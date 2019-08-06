import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s')
def timelogs():
    logging.debug(track())
    lines = [line.strip() for line in open('test.log')]
    for c in lines:
        M=c.split(',')
        print(M[0])