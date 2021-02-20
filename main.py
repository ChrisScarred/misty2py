from misty import Misty


mist = Misty("192.168.0.103")
cols = {
    "red": "0",
    "green": "0",
    "blue": "0"
}
r = mist.action('api/led', cols)
print(r)

r = mist.information('api/blink/settings')
print(r)