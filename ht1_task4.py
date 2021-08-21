uah = int(input('Enter the amount of hryvnia (uah): '))
rate_usd = float(input('Enter the current dollar (usd) rate: '))
usd = uah / rate_usd
print(round(usd, 2), 'dollars at the rate of', rate_usd, 'can be bought for', uah, 'hryvnas')