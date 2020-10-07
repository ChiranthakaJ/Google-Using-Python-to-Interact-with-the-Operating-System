import arrow

date = arrow.get('2020-10-03', 'YYYY-MM-DD')

print(date.shift(weeks=+6).format('MMM DD YYYY'))  #=====> Nov 14 2020