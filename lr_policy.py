"""
lr_policy in caffe
fixed: lr = base_lr
step: lr = base_lr*gamma^(floor(iter/step))
exp: lr = base_lr*gamma^iter
inv: lr = base_lr*(1+gamma*iter)^(-power)
multi_step: base_lr*gamma^p, where p is decided by different steps
poly: lr = base_lr*(1-iter/max_iter)^power
sigmoid: lr = base_lr/(1+exp(-gamma*(iter-step_size)))
"""
import math
import numpy as np
from figures import Line, Figure

lines = []
iters = np.linspace(1, 400, 400)
base_lr = 0.001
fixed_lr = np.ones(iters.shape[0])*base_lr
fixed_line = Line(label="fixed", data=fixed_lr, color="blue")
lines.append(fixed_line)

base_lr = 0.5
step_lr = base_lr*(0.969**np.floor(iters/2.))
step_line = Line(label="step", data=step_lr, color="red")
lines.append(step_line)

exp_lr = base_lr*(0.98**(iters-1))
exp_line = Line(label="exp", data=exp_lr, color="green")
lines.append(exp_line)

inv_lr = 2.0*((1+1.009**(iters-1))**(-2))
inv_line = Line(label="inv", data=inv_lr, color="magenta")
lines.append(inv_line)

multi_step_lr = base_lr*(0.126**np.floor(iters/100.))
multi_step_line = Line(label="multi-step", data=multi_step_lr, color="cyan")
lines.append(multi_step_line)

poly_lr = base_lr*((1-iters/np.max(iters))**0.75)
poly_line = Line(label="poly", data=poly_lr, color="orange")
lines.append(poly_line)

sigmoid_lr = base_lr / (1+np.exp(-0.02*(iters-200)))
sigmoid_line = Line(label="sigmoid", data=sigmoid_lr, color="purple")
lines.append(sigmoid_line)

fig = Figure(figure_name="lr_policy", xlabel="Epoch", ylabel="Learning rate")
fig.draw(lines)
