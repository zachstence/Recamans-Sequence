import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patches

def recaman(n):
  nums = []
  curr = 0
  for i in range(n):
    back = curr - i
    forward = curr + i
    if back > 0 and back not in nums:
      nums.append(back)
      curr = back
    else:
      nums.append(forward)
      curr = forward
  return nums


n = 100
# generate sequence
nums = recaman(n)

# fill centers and d(iameter)s lists for drawing arcs
centers = []
ds = []
start = nums[0]
for end in nums[1:]:
  centers.append((start + end) / 2)
  ds.append(end - start)
  start = end


fig, ax = plt.subplots()

# draw arcs
for c, d in zip(centers, ds):
  lw = 0.5
  arc = patches.Arc((c, 0), d, d, theta1=180, theta2=0, linewidth=lw)
  ax.add_patch(arc)

ax.set_frame_on(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)

v_buffer = 10
plt.xlim(0, max(nums))
plt.ylim(-1 * (max(ds) / 2 + v_buffer), max(ds) / 2 + v_buffer)

plt.gca().set_aspect('equal', adjustable='box')



fig.savefig('fig.png', bbox_inches='tight', dpi=1000)