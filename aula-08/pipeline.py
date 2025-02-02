from etl import pipeline_calc_kpi

# Running pipeline
pipeline_calc_kpi("data", ["csv", "parquet"])
