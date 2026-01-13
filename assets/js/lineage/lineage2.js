displayViz = {
  const width = 928;
  const height = 600;

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", dx)
      .attr("viewBox", [-marginLeft, -marginTop, width, dx])
      .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif; user-select: none;");
      
  const svgNode = svg`<svg width=${width + 200} height=${height + 200}></svg>`
  
  const svgSelection = d3.select(svgNode);

  const line = d3.line()
    .curve(d3.curveCatmullRom)
    .x(d => d.x * width)
    .y(d => d.y * height);

  const tooltip = d3.select("body").append("div")
    .attr("class", "svg-tooltip")
    .style("position", "absolute")
    .style("visibility", "hidden");

  const g = svgSelection.append('g').attr('transform', `translate(${100},${100})`)

  g.append('g')
    .selectAll('path')
    .data(links)
    .enter()
    .append('path')
    .attr('d', ({ source, target, data }) =>
      line([
        {
          x: source.x,
          y: source.y
        }
      ].concat(
        data.points || [],
        [{
          x: target.x,
          y: target.y
        }
        ])
      ))
    .attr('fill', 'none')
    .attr('stroke', 'black')
  
  const nodes = g.append('g')
    .attr("class", "nodes-g")
    .selectAll('g')
    .data(descendants)
    .enter()
    .append('g')
    .attr('transform', ({ x, y }) => `translate(${x * width}, ${y * height})`);

  nodes.append('circle')
    .attr('r', function (d) {
      const id = d.id.split(":")
      return id[0] == "module" ? modulesNodes : valueNodes
    })
    .attr('fill', function (d) {
      const id = d.id.split(":")
      return id[0] == "module" ? "#416ab6" : "#91acdf"
    }
    )
    .attr('stroke', 'black')


  // Add text, which screws up measureement
  nodes.append('text')
    .text(function (d) {
      const id = d.id.split(":")
      return id[0] == "module" ? d.data.desc.label : ""
    }
    )
    .style('font-family', 'Palanquin')
    .style('font-size', "10px")
    .attr('text-anchor', 'right')
    .attr('alignment-baseline', 'middle');

  nodes.on("mouseover", (e, d) => {
    tooltip.style("visibility", "visible");
  })
    .on("mousemove", (e, d) => {
      tooltip
        .style("top", (e.pageY - 10) + "px").style("left", (e.pageX + 10) + "px")

      const node_type = d.data.desc.node_type

      if (node_type == "operation") {
        tooltip.html(`Module name: ${d.data.desc.module_type}<br>Module author: ${d.data.info.authors.authors[0].name}<br>Module description: ${d.data.info.documentation.description}`);
      }

      else if (node_type == "value") {
        tooltip.html(`Value type: ${d.data.desc.data_type}<br>Value label: ${d.data.desc.label}<br>Value preview:<br> ${d.data.info.preview}`);
      }
    })
    .on("mouseout", () => {
      tooltip.style("visibility", "hidden");
    });

  yield svgNode;
}