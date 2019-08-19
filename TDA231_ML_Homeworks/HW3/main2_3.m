%%%%%%[ Question 2.3 ]%%%%%%%

% Task 2.2, Problem 2.3

clear all;
close all;

wd_coefficient = 0.0;
n_hid = 10;
n_iters = 70;
do_early_stopping = false;
mini_batch_size = 4;

momentums = [0 0.9];
learning_rates = [0.002 0.01 0.05 0.2 1.0 5.0 20.0];

%%

i = 0;
res = {};
for momentum_multiplier = momentums
	for learning_rate = learning_rates
		i = i + 1
		res{i}.momentum = momentum_multiplier;
		res{i}.learning_rate = learning_rate;
		res{i}.res = net(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size);
	end
end

%%
stats = zeros(14, 4);
for i = 1:14
	stats(i,:) = [i res{i}.learning_rate  res{i}.momentum res{i}.res.costs(1)];
end


