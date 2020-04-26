function density = fymarg(param,yik,i,k,N,K)

ai = param(i);  bk = param(N+k);  omegak = param(N+K+k);

zetaik = ai*bk/(omegak-1);  p = 1/omegak;

density = nbinpdf(yik,zetaik,p);  % compute the marginal density of y_{i,k}, f(y_{i,k}|theta)

end

