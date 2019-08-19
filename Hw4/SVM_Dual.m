
t = [1,1,1,-1,-1,-1];
x = [2,4,4,0,2,0; 2,4,0,0,0,2];

% Q = zeros(6);
% 
% Q = t.*x;
% Q = Q'*Q;
% 
% A = -ones(1,6);
% 
% c = ones(6,1);
% 
% z = zeros(6,1);
% 
% alpha = quadprog(Q,-c,-eye(6),z,t,0)
% 
% w = zeros(2,1);
% for i = 1:6
%     w = w+ alpha(i)*t(i)*x(:,i);
% end
% 
% 
% w

N = 6;

TX = t .* x;
H = TX' * TX;
f = -ones(N, 1);
A = -eye(N);
b = zeros(N, 1);
Aeq = t;% * eye(N, 1);
beq = 0;%zeros(N, 1);

alpha = quadprog(H, f, A, b, Aeq, 0);
