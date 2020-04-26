function Eloglikeik = ellk(param,wijk,chara,i,k,N,K,paramprime,Ybar)

% compute q(theta,theta',y_{i,k}) for each value of y_{i,k} from 0 to Ybar
smallqfun = zeros(Ybar+1,1);
for yik = 0:Ybar
    lwyjd = log(fwyjoint(param,wijk,chara,yik,i,k,N,K)+eps);  % +eps to prevent value too close to 0 that will cause numerical problem in taking the log
    ycd = fycond(wijk,chara,yik,i,k,N,K,paramprime,Ybar); 
    smallqfun(yik+1) = lwyjd*ycd;
end

% compute Sum_{y_{i,k}=0}^Ybar[q(theta,theta',y_{i,k})]
Eloglikeik = sum(smallqfun);

end

