function density = fwcond(param,wijk,chara,yik)

% b0 is alpha, b1 is the coef for logsize, b2 is the coef for logbtm, b3 is the coef for momentum
b0 = param(end-1-4); b1 = param(end-1-3); b2 = param(end-1-2); b3 = param(end-1-1);

% lambda_0 and lambda_1
lam0 = param(end-1); lam1 = param(end);  % lambda_{i,k} = lam0 + lam1*y_{i,k}

barwjk = b0+b1*chara(:,1)+b2*chara(:,2)+b3*chara(:,3);  % alpha+beta'X

dijk = (wijk>0)*1;  % indicator for w_{i,j,k}>0

% compute the conditional density f(w_{i,k}|y_{i,k},X_j,theta)
front = ( ((1/(lam0+lam1*yik))*normpdf((wijk-barwjk)/(lam0+lam1*yik))).^dijk );
backward = ( (normcdf(-barwjk/(lam0+lam1*yik))).^(1-dijk) );
density = prod( front.* backward);

end
