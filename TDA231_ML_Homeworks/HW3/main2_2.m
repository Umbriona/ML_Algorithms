%%%%%%[ Question 2.2 ]%%%%%%%

% Task 2.2

clear all;
close all;

wd_coefficient = 0;
n_hid = 10;
n_iters = 70;
learning_rate = 0.005;
momentum_multiplier = 0;
do_early_stopping = false;
mini_batch_size = 4;

%% (1)

res_1 = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

%% (2)
learning_rate = 0.5;
res_2 = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

%% (3)

momentum_multiplier = 0.9;
res_3 = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)

