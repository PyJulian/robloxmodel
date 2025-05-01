import random

model = '''<roblox version="4">
<Item class="Model">
  <Properties>
    <string name="Name">rng model</string>
  </Properties>
'''

try:
    f = open('/Users/yourname/Desktop/model.rbxmx', 'x')
except FileExistsError:
    f = open('/Users/yourname/Desktop/model.rbxmx', 'w')

for t in range(10):
    model += f'''
  <Item class="Part">
    <Properties>
      <string name="Name">Part</string>
      <Vector3 name="Position">
        <X>{random.randint(-10, 10)}</X>
        <Y>{random.randint(-10, 10)}</Y>
        <Z>{random.randint(-10, 10)}</Z>
      </Vector3>
      <Color3 name="Color">
        <R>{random.randint(0, 255)/255:.3f}</R>
        <G>{random.randint(0, 255)/255:.3f}</G>
        <B>{random.randint(0, 255)/255:.3f}</B>
      </Color3>
      <bool name="Anchored">true</bool>
      <bool name="CanCollide">true</bool>
      <Vector3 name="Size">
        <X>{random.randint(1, 10)}</X>
        <Y>{random.randint(1, 10)}</Y>
        <Z>{random.randint(1, 10)}</Z>
      </Vector3>
    </Properties>
  </Item>
'''

model += '''
</Item> <!-- Close Model -->
</roblox>
'''

f.write(model)
f.close()
