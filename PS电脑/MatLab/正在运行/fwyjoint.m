function density = fwyjoint(param,wijk,chara,yik,i,k,N,K)

wcdens = fwcond(param,wijk,chara,yik);  % compute f(w_{i,k}|y_{i,k},X_j,theta)
ymdens = fymarg(param,yik,i,k,N,K);  % compute f(y_{i,k}|theta)

density = wcdens.*ymdens;  % compute the joint density f(w_{i,k},y_{i,k}|X_j,theta)

end
