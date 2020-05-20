N = ЃП;
K = 8;


portweight = cell(N,K);
for i = 1:size(portweight,1)
    for j = 1:size(portweight,2)
        portweight{i,j} = str2num(portweightRaw(i,j))';
    end
end
% portweight

stockchara = cell(K,1);
for i = 1:size(stockchara,1)
    stockchara{i,1} = str2num(stockcharaRaw(i,1));
end
% stockchara

length = N+K+K+4+2;
initialparamval = rand(length,1);

%initialparamval




















% for i = 1:size(fund,1)
%     line = fund(i,:)';
%     for j = 1:size(cities,1)
% %         disp('Он')
%         province = cities(j);
%         for k = 1:10
%             code = line(2*i+2);
%             wgt = line(2*2+3);
%             
%             
% 
%         end
%     end
% end
% 
% 
% for i = 1:size(codes,1)
%     if code == codes(i,1)
%         print(code)
%     end
% end

    


