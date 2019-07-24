from tqdm import tqdm,trange
import time

# for i in tqdm(range(100)):
#     time.sleep(0.01)

# for i in trange(100):
#     time.sleep(0.01)

# for i in tqdm(list("abcdefgij"),desc="字母处理",unit="字母"):
#     time.sleep(1.2)

process = tqdm(total=50)
for i in range(10):
    time.sleep(0.5)
    process.update(5)
process.close()