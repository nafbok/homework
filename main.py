
uah = input('Enter the amount of hryvnia (uah): ')
rate_usd = input('Enter the current dollar (usd) rate: ')
if uah.isdigit() and rate_usd.isdigit():
    usd = uah / float(rate_usd)
print(usd, 'dollars at the rate of', rate_usd, 'can be bought for', uah, 'hryvnas')


