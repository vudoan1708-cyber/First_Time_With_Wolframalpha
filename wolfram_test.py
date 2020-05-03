import wolframalpha
print('Package Loaded')

# ask for users input
# python v2: raw_input
# python v3: input
input = str(input('Question: '))

# wolframalpha APP ID
APP_ID = 'WU4636-7HLUH76QPL'

# create a client
client = wolframalpha.Client(APP_ID);

# create a response
res = client.query(input)

answer = next(res.results).text
print(answer)