function density = fycond(wijk,chara,yik,i,k,N,K,paramprime,Ybar)

% evaluate f(w_{i,k},y_{i,k}|X_j,theta') under the current parameter estimate theta'
wikyjoint = fwyjoint(paramprime,wijk,chara,yik,i,k,N,K);

% obtain the value for f(w_{i,k}|X_j,theta') under the current parameter estimate theta'
wyjdens = zeros(Ybar+1,1);
for yval = 0:Ybar
    wyjdens(yval+1) = fwyjoint(paramprime,wijk,chara,yval,i,k,N,K); 
end
wikmarg = sum(wyjdens);

% obtain f(y_{i,k}|w_{i,k},X_j,theta') = f(w_{i,k},y_{i,k}|X_j,theta')/f(w_{i,k}|X_j,theta')
density = wikyjoint/(wikmarg+eps);  % +eps to prevent value too close to 0 that will cause numerical problem in the division

end
