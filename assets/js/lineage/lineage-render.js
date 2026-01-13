const d3 = window.d3;
const dagreD3 = window.dagreD3;

function makeNodeObj(relationObj) {
    return {
        shape: 'img',
        typeName: relationObj.typeName,
        label: relationObj.displayText.length > 18 ? relationObj.displayText.substring(0, 18) + '...' : relationObj.displayText,
        toolTipLabel: relationObj.displayText,
        id: relationObj.guid,
        isLineage: true,
        queryText: relationObj.queryText,
        status: relationObj.status,
    };
}

/**
 * 使用原生Javascript实现jQuery offset方法
 * https://www.jianshu.com/p/7816fbb216f4
 * @param {*} ele 
 * @returns 
 */
function offset(ele) {
    let result = {
        top: 0,
        left: 0,
    };
    let position;
    /*
    * nodeType 属性返回以数字值返回指定节点的节点类型。
    * 如果节点是元素节点，则 nodeType 属性将返回 1。
    * 如果节点是属性节点，则 nodeType 属性将返回 2。
    * 如果节点 node.nodeType 类型不是 Element(1)，则跳出；
    * 如果相关节点的 position 属性为 static，则不计入计算，进入下一个节点（其父节点）的递归。
    * 如果相关属性的 display 属性为 none，则应该直接返回 0 作为结果。
    */
    function getOffset(node, init) {
        if (node.nodeType !== 1) {
            return;
        }
        position = window.getComputedStyle(node)['position']
        if (typeof(init) === 'undefined' && position === 'static') {
            getOffset(node.parentNode)
            return;
        }
        result.top = node.offsetTop + result.top - node.scrollTop
        result.left = node.offsetLeft + result.left - node.scrollLeft
        if (position === 'fixed') {
            return;
        }
        getOffset(node.parentNode)
    }

    // 当前 DOM 节点的 display === 'none' 时, 直接返回 {top: 0, left: 0}
    if (window.getComputedStyle(ele)['display'] === 'none') {
        return result;
    }
    getOffset(ele, true);
    return result;
}

function fixScale(size) {
    if (size > 2) {
        return 2;
    }
    if (size < 0.8) {
        return 0.8;
    }
    return size;
}

function getTooltip(node, guid) {
    let htmlStr = '';
    if (node.id !== guid) {
        htmlStr = '<h5>' + (node.isLineage ? 'Lineage' : 'Impact') + '</h5>';
    } else {
        htmlStr = '<p style="margin: 0;">&nbsp;</p>';
    }
    htmlStr += '<p>guid: ' + node.id + '</p>';
    if (node.typeName) {
        htmlStr += '<p>type: ' + node.typeName + '</p>';
    }
    if (node.status) {
        htmlStr += '<p>status: ' + node.status + '</p>';
    }
    if (node.queryText) {
        htmlStr += '<p>query: <span style="color:#359f89">' + node.queryText + '</span></p> ';
    }
    htmlStr += '<p >content: <span style="color:#359f89">' + node.toolTipLabel + '</span></p>';
    return htmlStr;
}

function getImg(node, guid) {
    let type = node.isProcess || /process/.test(node.typeName) ? 'gear' : 'table';
    let status = /delete/i.test(node.status) ? '-delete' : (node.id === guid ? '-active' : '');
    return `../../static/images/lineage/icon-${type}${status}.png`;
}

const LineageLayoutView = {
    onRender: function(container, data) {
        this.container = container;
        this.guid = data.baseEntityGuid;
        this.g = new dagreD3.graphlib.Graph()
            .setGraph({
                nodesep: 50,
                ranksep: 90,
                rankdir: 'LR',
                marginx: 20,
                marginy: 20,
                transition: function(selection) {
                    return selection.transition().duration(500);
                }
            })
            .setDefaultEdgeLabel(function() {
                return {};
            });
        this.fromToObj = {};
        if (data.relations.length) {
            this.generateData(data.relations, data.guidEntityMap);
            this.createGraph();
        } else {
            this.noLineage();
        }
    },

    noLineage: function() {
        this.container.innerHTML = '<text x="50%" y="50%" alignment-baseline="middle" text-anchor="middle">No lineage data found</text>';
    },

    addNode: function(id, entity) {
        if (!this.fromToObj[id]) {
            this.fromToObj[id] = makeNodeObj(entity);
            this.g.setNode(id, this.fromToObj[id]);
        }
    },

    addPath: function(fromEntityId, toEntityId, id, stroke) {
        this.g.setEdge(fromEntityId, toEntityId, {
            arrowhead: 'arrowPoint', 
            lineInterpolate: 'basis',
            style: 'fill: none; stroke: ' + stroke + '; stroke-width: 2',
            stroke,
            id,
        });
    },

    generateData: function(relations, guidEntityMap) {
        let that = this;

        relations.forEach(function(obj) {
            that.addNode(obj.fromEntityId, guidEntityMap[obj.fromEntityId]);
            that.addNode(obj.toEntityId, guidEntityMap[obj.toEntityId]);
            that.addPath(obj.fromEntityId, obj.toEntityId, obj.relationshipId, '#8bc152');
        });

        if (this.fromToObj[this.guid]) {
            this.fromToObj[this.guid].isLineage = false;
            this.checkForLineageOrImpactFlag(relations, this.guid);
        }
    },

    checkForLineageOrImpactFlag: function(relations, guid) {
        let that = this;
        relations.forEach(function(node) {
            if (!node.traversed && node.fromEntityId === guid) {
                node.traversed = true;
                that.fromToObj[node.toEntityId].isLineage = false;
                that.addPath(node.fromEntityId, node.toEntityId, node.relationshipId, '#fb4200');
                that.checkForLineageOrImpactFlag(relations, node.toEntityId);
            }
        });
    },

    getGraphZoomPositionCal: function(zoom) {
        let initialScale = 1.2,
            svgEl = this.container,
            translateValue = [
                (this.container.clientWidth - this.g.graph().width * initialScale) / 2, 
                (this.container.clientHeight - this.g.graph().height * initialScale) / 2
            ];
        if (Object.keys(this.g._nodes).length > 15) {
            initialScale = 0;
            svgEl.classList.add('noScale');
        }
        zoom.translate(translateValue).scale(fixScale(initialScale));
    },

    zoomed: function(zoom) {
        this.container.firstElementChild.setAttribute('transform', 'translate(' + zoom.translate() + ')' + 'scale(' + fixScale(zoom.scale()) + ')');
    },

    createGraph: function() {
        let that = this,
            width = this.container.clientWidth,
            height = this.container.clientHeight;

        this.g.nodes().forEach(function(v) {
            let node = that.g.node(v);
            // Round the corners of the nodes
            if (node) {
                node.rx = node.ry = 5;
            }
        });

        // Create the renderer
        let aRender = new dagreD3.render();

        // Add our custom arrow (a hollow-point)
        aRender.arrows().arrowPoint = function normal(parent, id, edge, type) {
            let marker = parent.append('marker')
                .attr('id', id)
                .attr('viewBox', '0 0 10 10')
                .attr('refX', 9)
                .attr('refY', 5)
                .attr('markerUnits', 'strokeWidth')
                .attr('markerWidth', 10)
                .attr('markerHeight', 8)
                .attr('orient', 'auto');

            let path = marker.append('path')
                .attr('d', 'M 0 0 L 10 5 L 0 10 z')
                .style('stroke-width', 1)
                .style('stroke-dasharray', '1,0')
                .style('fill', edge.stroke)
                .style('stroke', edge.stroke);
            dagreD3.util.applyStyle(path, edge[type + 'Style']);
        };

        aRender.shapes().img = function(parent, bbox, node) {
            let currentNode = node.id == that.guid;
            let shapeSvg = parent.append('circle')
                .attr('fill', 'url(#img_' + node.id + ')')
                .attr('r', currentNode ? '15px' : '14px')
                .attr('class', 'nodeImage ' + (currentNode ? 'currentNode' : (node.isProcess ? 'blue' : 'green')));

            parent.insert('defs')
                .append('pattern')
                .attr('x', '0%')
                .attr('y', '0%')
                .attr('patternUnits', 'objectBoundingBox')
                .attr('id', 'img_' + node.id)
                .attr('width', '100%')
                .attr('height', '100%')
                .append('image')
                .attr('xlink:href', function() {
                    return node && getImg(node, that.guid);
                })
                .attr('x', '2')
                .attr('y', '2')
                .attr('width', currentNode ? '26' : '24')
                .attr('height', currentNode ? '26' : '24')

            node.intersect = function(point) {
                return dagreD3.intersect.circle(node, currentNode ? 16 : 13, point);
            };
            return shapeSvg;
        };

        // Set up an SVG group so that we can translate the final graph.
        const svg = d3.select(this.container)
            .attr('viewBox', '0 0 ' + width + ' ' + height)
            .attr('enable-background', 'new 0 0 ' + width + height);

        const svgGroup = svg.append('g');

        const zoom = d3.behavior.zoom().scaleExtent([0.5, 6]).on('zoom', function() {
            that.zoomed(zoom);
        });
    
        d3.selectAll('[data-zoom]').on('click', function() {
            let direction = 1,
                factor = 0.2,
                target_zoom = 1,
                center = [that.g.graph().width / 2, that.g.graph().height / 2],
                extent = zoom.scaleExtent(),
                translate = zoom.translate(),
                translate0 = [],
                l = [],
                view = { x: translate[0], y: translate[1], k: zoom.scale() };

            d3.event.preventDefault();
            direction = +this.getAttribute('data-zoom');
            target_zoom = zoom.scale() * (1 + factor * direction);

            if (target_zoom < extent[0] || target_zoom > extent[1]) {
                return false;
            }

            translate0 = [(center[0] - view.x) / view.k, (center[1] - view.y) / view.k];
            view.k = target_zoom;
            l = [translate0[0] * view.k + view.x, translate0[1] * view.k + view.y];

            view.x += center[0] - l[0];
            view.y += center[1] - l[1];

            return d3.transition().duration(350).tween('zoom', function() {
                let iTranslate = d3.interpolate(zoom.translate(), [view.x, view.y]),
                    iScale = d3.interpolate(zoom.scale(), view.k);
                return function(t) {
                    zoom.scale(fixScale(iScale(t))).translate(iTranslate(t));
                    that.zoomed(zoom);
                };
            });
        });

        let tooltip = d3.tip()
            .attr('class', 'd3-tip')
            .offset([10, 0])
            .html((d) => getTooltip(that.g.node(d), that.guid));

        svg.call(zoom).call(tooltip);

        aRender(svgGroup, this.g);

        svg.on('dblclick.zoom', null).on('wheel.zoom', null);

        //change text postion 
        svgGroup.selectAll('g.nodes g.label').attr('transform', 'translate(2,-30)');

        svgGroup.selectAll('g.nodes g.node').on('mouseenter', function(d) {
            that.activeNode = true;

            // Fix
            let width2 = document.body.clientWidth;
            let currentOffset = offset(this);
            let direction = 'e';
            if (((width2 - currentOffset.left) < 330)) {
                direction = (((width2 - currentOffset.left) < 330) && ((currentOffset.top) < 400)) ? 'sw' : 'w';
                if (((width2 - currentOffset.left) < 330) && ((currentOffset.top) > 600)) {
                    direction = 'nw';
                }
            } else if (((currentOffset.top) > 600)) {
                direction = (((width2 - currentOffset.left) < 330) && ((currentOffset.top) > 600)) ? 'nw' : 'n';
                if ((currentOffset.left) < 50) {
                    direction = 'ne'
                }
            } else if ((currentOffset.top) < 400) {
                direction = ((currentOffset.left) < 50) ? 'se' : 's';
            }
            tooltip.direction(direction).show(d, this);
        })
        .on('dblclick', function(d) {
            tooltip.hide(d);
            console.log('go to detail view', d);
        }).on('mouseleave', function(d) {
            that.activeNode = false;
            setTimeout(function() {
                if (!that.activeTip && !that.activeNode) {
                    tooltip.hide(d);
                }
            }, 400);
        });

        svgGroup.selectAll('g.edgePath path.path').on('click', function(d) {
            console.log('go to detail view', d);
        });

        // Center the graph
        this.getGraphZoomPositionCal(zoom);

        zoom.event(svg);
    }
};
