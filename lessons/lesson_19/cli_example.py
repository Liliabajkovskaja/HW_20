import argparse


parser = argparse.ArgumentParser()

parser.add_argument('name', help='Enter your name')  # positional args
parser.add_argument('--position', '-p', help='Enter your position', required=True)
parser.add_argument('--salary', '-s', help='Set your salary', type=int)
parser.add_argument('--UAH', help='Is it UAH', action="store_true")


if __name__ == '__main__':
    args = parser.parse_args()
    print(args.name)
    print(args.position)
    if args.UAH:
        print(args.salary * 38)
    else:
        print(args.salary)