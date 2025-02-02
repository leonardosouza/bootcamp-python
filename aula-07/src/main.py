from etl import filter_delivered, filter_sum_totals, processing_data, read_csv

# Soma de todos os produtos
print(filter_sum_totals(processing_data(read_csv("sales.csv"))))

# Soma dos produtos entregues
print(filter_sum_totals(filter_delivered(processing_data(read_csv("sales.csv")))))
