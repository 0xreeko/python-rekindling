from time import sleep
counter = 0
deposit = 50
apy = 0.2

while counter < 30:
    deposit += deposit * apy  # using a different pointer prevents loop update
    counter += 1
    print(f"Day {counter}: £{deposit}")
    sleep(0.5)
