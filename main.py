from misty.robot import Misty


misty_robot = Misty("192.168.0.103")
cols = {
    "red": "0",
    "green": "0",
    "blue": "0"
}
r = misty_robot.perform_action('api/led', cols)
print(r)

r = misty_robot.get_info('blink_settings')
print(r)

print(misty_robot)
