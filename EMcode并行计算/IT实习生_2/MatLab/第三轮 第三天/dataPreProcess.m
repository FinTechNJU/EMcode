clc
clear

N = 100;
K = 3;
% name_array = fund(:,3);

portweight = cell(N,K);
for i = 1:size(portweight,1)
    for j = 1:size(portweight,2)
        portweight{i,j} = str2num(portweightfew(i,j))';
    end
end
% portweight

stockchara = cell(K,1);
for i = 1:size(stockchara,1)
    stockchara{i,1} = str2num(stockcharafew(i,1));
end
% stockchara

length = N+K+K+4+2;
initialparamval = ones(length,1)/10;
for i = N+K+1:N+K+K
    initialparamval(i) = 5;
end
%initialparamval





