%% Part 1: import data and set up things
clear all;
close all;

% load the portfolio weight data
% the portfolio weight data needs to be in an NxK Matlab cell structure called portweight, 
% where in each {i,k} cell is a (J_k x 1) vector that contains J_k number of observations of w_{i,j,k} for investor i in city k
load('portweight.mat');
[N,K] = size(portweight);

% load the stock characteristics data
% the stock characteristics data needs to be in a Kx1 Matlab cell structure called stockchara,
% where in each {k} cell is a (J_k x 3) matrix that contains the observations for the characteristics X_j of the stocks j in city k
load('stockchara.mat');

% import initial parameter values (theta_0)
% this is a (N+K+K+4+2)x1 vector called initialparamval
load('initialparamval.mat');

% set up parameter bounds
L = [0.01*ones(N,1);0.001*ones(K,1);1.0*ones(K,1);-10*ones(4,1);0.0001*ones(2,1)];  % lower bound
H = [1000*ones(N,1);0.9*ones(K,1);10*ones(K,1);10*ones(4,1);10*ones(2,1)];  % upper bound

% set up the equality constraint for b_k --- the normalization condition of the sum of b_k equal to 1
Aeq = [zeros(1,N),ones(1,K),zeros(1,K+4+2)];  beq = 1;

% set up the upper limit for the summation over y_{i,k}, i.e.\ the value that replaces +infinity
Ybar = 50;

% set up convergence criterion for the EM algorithm
convergcrit = 1e-3;


%% Part 2: execution of the main EM algorithm

% set up the Matlab minimization fmincon routine with the interior point algorithm and the first-order optimality measure equal to 1e-4
optim_options = optimset('Algorithm','interior-point','Display','off','TolX',1e-4,'TolFun',1e-4,'MaxFunEvals',5000,'MaxIter',5000);

% % Iteration 1
% let theta' = theta_0
paramprime = initialparamval;
% E-step to obtain Q(theta,theta'); then negate it to get -Q(theta,theta') for the fmincon routine
objfun = @(param)(-Qfun(param,portweight,stockchara,N,K,paramprime,Ybar));
% M-step to obtain the new estimate hat{theta}_1
[param_est] = fmincon(objfun,paramprime,[],[],Aeq,beq,L,H,[],optim_options);
% get the difference D_s = |Q(hat{theta}_1,hat{theta}_1) - Q(theta_0,theta_0)| for convergence checking
Ds = abs(Qfun(param_est,portweight,stockchara,N,K,param_est,Ybar) - Qfun(paramprime,portweight,stockchara,N,K,paramprime,Ybar));

% Checking for convergence of the EM algorithm, 
% if Ds<=convergcrit, concludes the iterative process, otherwise continue to the next iteration
while Ds>convergcrit
    % % Iteration s, s>=2
    % let theta' = hat{theta}_{s-1}
    paramprime = param_est;
    % repeat the E-step and negation to obtain -Q(theta,theta')
    objfun = @(param)(-Qfun(param,portweight,stockchara,N,K,paramprime,Ybar));
    % repeat the M-step to obtain the new estimate hat{theta}_s
    [param_est] = fmincon(objfun,paramprime,[],[],Aeq,beq,L,H,[],optim_options);
    % get the difference D_s for convergence checking
    Ds = abs(Qfun(param_est,portweight,stockchara,N,K,param_est,Ybar) - Qfun(paramprime,portweight,stockchara,N,K,paramprime,Ybar));
end

% after the EM algorithm finishes, obtain the final parameter estimate theta_MLE
thetaMLE = param_est;

