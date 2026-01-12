from SchemaAnalyzer import SchemaAnalyzer


analyzer = SchemaAnalyzer(
    host = 'localhost',
    user = 'root',
    password = 'MswG@2024',
    database = 'bi_data',
    port = 3306
)

analyzer.analyze_schema()
schema = analyzer.get_schema()
table_name_list = list(schema.keys())

print(', '.join(table_name_list))
print("\n")

print("ads_sport_live_collect_dd schema:")
print(schema['ads_sport_live_collect_dd'])