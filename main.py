from misty.robot import Misty


misty_robot = Misty("192.168.0.103")

r = misty_robot.perform_action('led', string="led_off", method="string")
print(r)

r = misty_robot.get_info('blink_settings')
print(r)

print(misty_robot)
