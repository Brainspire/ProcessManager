import argparse,time

parser = argparse.ArgumentParser(description='test process')
parser.add_argument('sleep', type=int, help='integer defining length of time to sleep', default=10)

args = parser.parse_args()

time.sleep(args.sleep)

print("process complete")
