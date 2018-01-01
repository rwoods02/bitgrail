#!/usr/bin/env python
import argparse
import bitgrail


def main():
    parser = argparse.ArgumentParser(description='Dashoboard is used to perform Bitgrail API operations')
    parser.add_argument('-r', '--request', type=str, required=True,
                        help='http operation to perform only get or post are supported')
    parser.add_argument('-e', '--endpoint', type=str, required=True,
                        help='http endpoint to append to url')
    parser.add_argument('-c', '--coin', type=str, default=None,
                        help='coin or pair to reference')
    parser.add_argument('-p', '--pair', type=str, default=None,
                        help='trading pair to reference')
    parser.add_argument('-a', '--amount', type=str, default=None,
                        help='amount to buy, sell, or withdraw')
    parser.add_argument('--address', type=str, default=None,
                        help='address of wallet to withdraw')
    parser.add_argument('--uuid', type=str, default=None,
                        help='id for the transaction for cancel orders')

    args = parser.parse_args()
    bg = bitgrail.Bitgrail()

    # Perform request
    if args.request == 'get':
        print "Output from public get request"
        bg.get(args.endpoint, args.pair)
    elif args.request == 'post':
        print "Output from private post request "
        bg.post(args.endpoint, args.coin, args.amount, args.address, args.uuid)
    else:
        print "Invalid request parameter. Please \"get\" or \"post\""


if __name__ == "__main__":
    main()
