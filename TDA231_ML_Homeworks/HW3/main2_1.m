%%%%%%[ Question 2.1 ]%%%%%%%

% Task 2.1, Problem 2.2

clear all;
close all;

wd_coefficient = 0.1;
n_hid = 7;
n_iters = 10;
learning_rate = 0;
momentum_multiplier = 0;
do_early_stopping = false;
mini_batch_size = 4;

%%

res = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)