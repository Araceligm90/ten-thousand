# CHAT GPT CODE 

**1. Prompt that I used to generate code:**

'Can you please give me a number randomizer that returns a tuple?'

**2. Actual code that ChatGPT provided:**

    import random

    def generate_random_tuple(length):
       # Generate a list of random numbers
       nums = [random.randint(1, 100) for _ in range(length)]
       # Convert the list to a tuple and return it
       return tuple(nums)

    my_tuple = generate_random_tuple(6)
    print(my_tuple)

