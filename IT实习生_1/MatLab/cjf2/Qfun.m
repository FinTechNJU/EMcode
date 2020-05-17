function loglikeval = Qfun(param,portweight,stockchara,N,K,paramprime,Ybar)

% compute Sum_{y_{i,k}=0}^Ybar[q(theta,theta',y_{i,k})] for every investor-city {i,k} pair
Eloglike = zeros(N,K);
for i = 1:N
    for k = 1:K
        wijk = portweight{i,k};
        chara = stockchara{k};
        Eloglike(i,k) = ellk(param,wijk,chara,i,k,N,K,paramprime,Ybar);
    end
end

% compute Q(theta,theta') = Sum_{i=1}^N Sum_{k=1}^K [ Sum_{y_{i,k}=0}^Ybar[q(theta,theta',y_{i,k})] ]
loglikeval = sum(sum(Eloglike,2));

end
