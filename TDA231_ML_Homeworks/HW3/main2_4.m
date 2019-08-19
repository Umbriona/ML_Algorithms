%%%%%%[ Question 2.4 ]%%%%%%%

% Task 2.2, Problem 2.4

clear all;
close all;

wd_coefficient = 0;
n_hid = 200;
n_iters = 1000;
learning_rate = 0.35;
momentum_multiplier = 0.9;
do_early_stopping = false;
mini_batch_size = 100;

%% (a)

res_a = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

%% (b)

do_early_stopping = true;
res_b = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

%% (c)

do_early_stopping = false;
res_c = {};
i = 0;
for param = [10 1 0.0001 0.001 5]
	i = i + 1;
	res_c{i} = net(param, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)
end

%% (d)

wd_coefficient = 0;
res_d = {};
i = 0;
for param = [10 30 100 130 200]
	i = i + 1;
	res_d{i} = net(wd_coefficient, param, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)
end

%% (e)

do_early_stopping = true;
i = 0;
res_e = {};
for param = [18 37 83 113 236]
	i = i + 1;
	res_e{i} = net(wd_coefficient, param, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)
end

%% (f)

wd_coefficient = 0;
n_hid = 37;
n_iters = 1000;
learning_rate = 0.2;
momentum_multiplier = 0.9;
do_early_stopping = true;
mini_batch_size = 100;
no_wd = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

wd_coefficient = 0.001
with_wd = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)
