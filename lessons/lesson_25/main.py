import os

print('script inside docker was run')

import time
import os


if not os.path.exists('asd'):
    os.mkdir('asd')

with open(os.path.join('asd', 'logs.txt'), 'a') as f:
    f.write(str(time.time()))