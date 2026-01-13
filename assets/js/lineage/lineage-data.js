window.lineageData = {
    "baseEntityGuid": "93028247-dcd0-44dc-9e80-432173dae664",
    "lineageDirection": "BOTH",
    "lineageDepth": 3,
    "guidEntityMap": {
        "2f3fd4c7-74dd-4b1c-8357-8cc7c7782c36": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hive",
                "createTime": 1646188358000,
                "qualifiedName": "default.qx_pricing_factor@dizhistg",
                "name": "qx_pricing_factor",
                "description": null
            },
            "guid": "2f3fd4c7-74dd-4b1c-8357-8cc7c7782c36",
            "status": "ACTIVE",
            "displayText": "qx_pricing_factor",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "29f90ee2-07d0-48d1-a6c7-5823d1bb3f18": {
            "typeName": "sqoop_dbdatastore",
            "attributes": {
                "owner": "hdfs",
                "createTime": null,
                "qualifiedName": "mysql --url jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity",
                "name": "mysql --url jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity",
                "description": ""
            },
            "guid": "29f90ee2-07d0-48d1-a6c7-5823d1bb3f18",
            "status": "ACTIVE",
            "displayText": "mysql --url jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "74f8db88-112d-4cd5-8989-91e04001dd65": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hdfs",
                "createTime": 1646277920000,
                "qualifiedName": "default.qx_cps_backup_04@dizhistg",
                "name": "qx_cps_backup_04",
                "description": null
            },
            "guid": "74f8db88-112d-4cd5-8989-91e04001dd65",
            "status": "ACTIVE",
            "displayText": "qx_cps_backup_04",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "93028247-dcd0-44dc-9e80-432173dae664": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hdfs",
                "createTime": 1646196657000,
                "qualifiedName": "default.qx_cps_backup_03@dizhistg",
                "name": "qx_cps_backup_03",
                "description": null
            },
            "guid": "93028247-dcd0-44dc-9e80-432173dae664",
            "status": "ACTIVE",
            "displayText": "qx_cps_backup_03",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "c029dc76-2a90-4a72-81a9-bf3d5241eba1": {
            "typeName": "hive_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "LOAD:hdfs:dizhistguserhdfsqx_commodity@dizhistg->:default.qx_commodity@dizhistg:1646186787000",
                "name":"load data inpath hdfs://dizhistg/user/hdfs/qx_commodity overwrite into table `default`.`qx_commodity`",
                "description": null
            },
            "guid": "c029dc76-2a90-4a72-81a9-bf3d5241eba1",
            "status": "ACTIVE",
            "displayText":"load data inpath hdfs://dizhistg/user/hdfs/qx_commodity overwrite into table `default`.`qx_commodity`",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "48ee0c0d-3545-4909-9fce-7a244e608e73": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hdfs",
                "createTime": 1646189769000,
                "qualifiedName": "default.qx_cps_backup@dizhistg",
                "name": "qx_cps_backup",
                "description": null
            },
            "guid": "48ee0c0d-3545-4909-9fce-7a244e608e73",
            "status": "ACTIVE",
            "displayText": "qx_cps_backup",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "ab2dc10e-726c-4034-9cfb-89e47da7b7ac": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hdfs",
                "createTime": 1646189557000,
                "qualifiedName": "default.qx_cps@dizhistg",
                "name": "qx_cps",
                "description": null
            },
            "guid": "ab2dc10e-726c-4034-9cfb-89e47da7b7ac",
            "status": "ACTIVE",
            "displayText": "qx_cps",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "9e91855a-4afd-4b85-9d05-1a1e7ab56d85": {
            "typeName": "hive_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "default.qx_cps_backup_03@dizhistg:1646196657000",
                "name": "create table qx_cps_backup_03 as\\nselect qc.* from qx_cps_backup qcb,qx_commodity qc where qcb.code = qc.code",
                "description": null
            },
            "guid": "9e91855a-4afd-4b85-9d05-1a1e7ab56d85",
            "status": "ACTIVE",
            "displayText": "create table qx_cps_backup_03 as\\nselect qc.* from qx_cps_backup qcb,qx_commodity qc where qcb.code = qc.code",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "93d1636f-ed82-4170-845c-104063dcd37f": {
            "typeName": "hive_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "default.qx_cps_backup@dizhistg:1646189769000",
                "name": "create table  qx_cps_backup as\\nselect * from qx_cps",
                "description": null
            },
            "guid": "93d1636f-ed82-4170-845c-104063dcd37f",
            "status": "ACTIVE",
            "displayText": "create table  qx_cps_backup as\\nselect * from qx_cps",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "ac65a747-b0f7-4c64-b37e-53e93020c191": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hive",
                "createTime": 1646187485000,
                "qualifiedName": "default.qx_sku@dizhistg",
                "name": "qx_sku",
                "description": null
            },
            "guid": "ac65a747-b0f7-4c64-b37e-53e93020c191",
            "status": "ACTIVE",
            "displayText": "qx_sku",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "56dfc579-e00f-4257-b4ef-26d7b96100d1": {
            "typeName": "hive_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "default.qx_cps_backup_04@dizhistg:1646277920000",
                "name": "create table qx_cps_backup_04 as \\nselect 1 from qx_commodity qc,qx_cps_backup_03 qcb3,qx_sku qs where qc.commodity_type = qcb3.commodity_type and qc.code = qs.commodity_code limit 1",
                "description": null
            },
            "guid": "56dfc579-e00f-4257-b4ef-26d7b96100d1",
            "status": "ACTIVE",
            "displayText": "create table qx_cps_backup_04 as \\nselect 1 from qx_commodity qc,qx_cps_backup_03 qcb3,qx_sku qs where qc.commodity_type = qcb3.commodity_type and qc.code = qs.commodity_code limit 1",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "dfdeddc3-6ac2-4828-badc-3bc3cda182d7": {
            "typeName": "hive_table",
            "attributes": {
                "owner": "hive",
                "createTime": 1646186787000,
                "qualifiedName": "default.qx_commodity@dizhistg",
                "name": "qx_commodity",
                "description": null
            },
            "guid": "dfdeddc3-6ac2-4828-badc-3bc3cda182d7",
            "status": "ACTIVE",
            "displayText": "qx_commodity",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "e9327df5-8dcf-4569-8a80-fbabea086cbf": {
            "typeName": "hive_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "default.qx_cps@dizhistg:1646189557000",
                "name": "create table  qx_cps as\\nselect qc.* from qx_commodity qc,qx_sku qs,qx_pricing_factor qpf where qc.code = qs.commodity_code and qc.code = qpf.commodity_code",
                "description": null
            },
            "guid": "e9327df5-8dcf-4569-8a80-fbabea086cbf",
            "status": "ACTIVE",
            "displayText": "create table  qx_cps as\\nselect qc.* from qx_commodity qc,qx_sku qs,qx_pricing_factor qpf where qc.code = qs.commodity_code and qc.code = qpf.commodity_code",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "d89b1f4b-def0-49f8-8a10-171429b76c11": {
            "typeName": "hdfs_path",
            "attributes": {
                "owner": null,
                "createTime": 0,
                "qualifiedName": "hdfs://dizhistg/user/hdfs/qx_commodity@dizhistg",
                "name": "/user/hdfs/qx_commodity",
                "description": null
            },
            "guid": "d89b1f4b-def0-49f8-8a10-171429b76c11",
            "status": "ACTIVE",
            "displayText": "/user/hdfs/qx_commodity",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        },
        "67763977-a3eb-47f4-bf34-274513bae327": {
            "typeName": "sqoop_process",
            "attributes": {
                "owner": null,
                "createTime": null,
                "qualifiedName": "sqoop import --connect jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity --hive-import --hive-database default --hive-table qx_commodity --hive-cluster dizhistg",
                "name": "sqoop import --connect jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity --hive-import --hive-database default --hive-table qx_commodity --hive-cluster dizhistg",
                "description": null
            },
            "guid": "67763977-a3eb-47f4-bf34-274513bae327",
            "status": "ACTIVE",
            "displayText": "sqoop import --connect jdbc:mysql://172.16.212.69:3306/noah?allowLoadLocalInfile=false&autoDeserialize=false&allowLocalInfile=false&allowUrlInLocalInfile=false&zeroDateTimeBehavior=convertToNull --table qx_commodity --hive-import --hive-database default --hive-table qx_commodity --hive-cluster dizhistg",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": []
        }
    },
    "relations": [
        {
            "fromEntityId": "9e91855a-4afd-4b85-9d05-1a1e7ab56d85",
            "toEntityId": "93028247-dcd0-44dc-9e80-432173dae664",
            "relationshipId": "427bfbef-5d01-404b-aeb2-1f82668ca9ac"
        },
        {
            "fromEntityId": "ac65a747-b0f7-4c64-b37e-53e93020c191",
            "toEntityId": "e9327df5-8dcf-4569-8a80-fbabea086cbf",
            "relationshipId": "216a8e18-79f9-42e4-b0eb-55327ad590a6"
        },
        {
            "fromEntityId": "56dfc579-e00f-4257-b4ef-26d7b96100d1",
            "toEntityId": "74f8db88-112d-4cd5-8989-91e04001dd65",
            "relationshipId": "d9a015cd-a6fb-45ee-a7e9-430e01d60f0f"
        },
        {
            "fromEntityId": "e9327df5-8dcf-4569-8a80-fbabea086cbf",
            "toEntityId": "ab2dc10e-726c-4034-9cfb-89e47da7b7ac",
            "relationshipId": "7830c377-d099-4b8f-b2e4-e623e4726c7b"
        },
        {
            "fromEntityId": "dfdeddc3-6ac2-4828-badc-3bc3cda182d7",
            "toEntityId": "9e91855a-4afd-4b85-9d05-1a1e7ab56d85",
            "relationshipId": "da7d187c-6764-4359-9593-3df7cb3905cc"
        },
        {
            "fromEntityId": "67763977-a3eb-47f4-bf34-274513bae327",
            "toEntityId": "dfdeddc3-6ac2-4828-badc-3bc3cda182d7",
            "relationshipId": "71b77d94-be1f-44b9-9800-126b9abe97d4"
        },
        {
            "fromEntityId": "ab2dc10e-726c-4034-9cfb-89e47da7b7ac",
            "toEntityId": "93d1636f-ed82-4170-845c-104063dcd37f",
            "relationshipId": "e48d7bd5-6592-4a19-8d76-73831c134cd7"
        },
        {
            "fromEntityId": "c029dc76-2a90-4a72-81a9-bf3d5241eba1",
            "toEntityId": "dfdeddc3-6ac2-4828-badc-3bc3cda182d7",
            "relationshipId": "88b3aa79-9d29-428e-94c9-be619ad7c58a"
        },
        {
            "fromEntityId": "2f3fd4c7-74dd-4b1c-8357-8cc7c7782c36",
            "toEntityId": "e9327df5-8dcf-4569-8a80-fbabea086cbf",
            "relationshipId": "8aa72b61-a976-48f8-945d-a517164661c2"
        },
        {
            "fromEntityId": "29f90ee2-07d0-48d1-a6c7-5823d1bb3f18",
            "toEntityId": "67763977-a3eb-47f4-bf34-274513bae327",
            "relationshipId": "2edab43a-53cf-458a-ad8d-88c3cf8756f9"
        },
        {
            "fromEntityId": "93028247-dcd0-44dc-9e80-432173dae664",
            "toEntityId": "56dfc579-e00f-4257-b4ef-26d7b96100d1",
            "relationshipId": "d7f09a76-fe78-4371-80d8-501e1313655d"
        },
        {
            "fromEntityId": "93d1636f-ed82-4170-845c-104063dcd37f",
            "toEntityId": "48ee0c0d-3545-4909-9fce-7a244e608e73",
            "relationshipId": "c983451e-a83a-4d77-bd01-5cb7fd3ed16e"
        },
        {
            "fromEntityId": "48ee0c0d-3545-4909-9fce-7a244e608e73",
            "toEntityId": "9e91855a-4afd-4b85-9d05-1a1e7ab56d85",
            "relationshipId": "968d3aa0-8595-4779-b9b4-51859167ae05"
        },
        {
            "fromEntityId": "d89b1f4b-def0-49f8-8a10-171429b76c11",
            "toEntityId": "c029dc76-2a90-4a72-81a9-bf3d5241eba1",
            "relationshipId": "ccffbc30-0d6a-4e3d-adda-0e8a8eccc404"
        },
        {
            "fromEntityId": "dfdeddc3-6ac2-4828-badc-3bc3cda182d7",
            "toEntityId": "e9327df5-8dcf-4569-8a80-fbabea086cbf",
            "relationshipId": "6823b0d4-874e-4f90-857a-07a6dfe35b05"
        }
    ]
};
