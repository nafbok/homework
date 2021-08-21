uah = int(input('Enter the amount of hryvnia (uah): '))
rate_usd = float(input('Enter the current dollar (usd) rate: '))
if rate_usd > 0:
    usd = uah / rate_usd
    print(round(usd, 2), 'dollars at the rate of', rate_usd, 'can be bought for', uah, 'hryvnas')
else:
    print(rate_usd, 'Not valid usd rate')