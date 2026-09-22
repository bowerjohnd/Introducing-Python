#====================================================
# 21- (ETL) - Extracting, Transforming, and Loading
#       using petl and pandas
#====================================================

# bubbles is deprecated... asking google AI for another ETL
#import bubbles

#p = bubbles.Pipeline()
#p.source(bubbles.data_object('csv_source', 'zoo.csv', infer_fields=True))
#p.aggregate('animal', 'hush')
#p.pretty_print()


# petl - similar to bubbles pretty_print, but seems a bit of work to get it
import petl as etl

pipe = etl.fromcsv('zoo.csv')
pipe = etl.aggregate(pipe, 
            key='animal', 
            aggregation={'hush_sum': ('hush', lambda values: sum(int(v) for v in values if v)), 
                        'hush_count': ('hush', lambda values: len(list(values)))})
pipe = etl.sort(pipe, key='hush_sum', reverse=True)

#print(etl.look(pipe))

# pandas - much less work than petl
import pandas as pd

df = pd.read_csv('zoo.csv')
aggregated_df = df.groupby('animal')['hush'].sum().reset_index()
sorted_df = aggregated_df.sort_values(by='hush', ascending=False)

print("=" * 50)
print(aggregated_df.to_string(index=False))
print("=" * 50)
print(sorted_df.to_markdown(index=False, tablefmt="grid"))  # requires pip install tabulate
print("=" * 50)
