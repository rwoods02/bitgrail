# bitgrail
Using the bitgrail API 

usage: dashboard.py [-h] -r REQUEST -e ENDPOINT [-c COIN] [-p PAIR]
                    [-a AMOUNT] [--address ADDRESS] [--uuid UUID]

Dashoboard is used to perform Bitgrail API operations

optional arguments:
  -h, --help            show this help message and exit
  -r REQUEST, --request REQUEST
                        http operation to perform only get or post are
                        supported
  -e ENDPOINT, --endpoint ENDPOINT
                        http endpoint to append to url
  -c COIN, --coin COIN  coin or pair to reference
  -p PAIR, --pair PAIR  trading pair to reference
  -a AMOUNT, --amount AMOUNT
                        amount to buy, sell, or withdraw
  --address ADDRESS     address of wallet to withdraw
  --uuid UUID           id for the transaction for cancel orders
 
