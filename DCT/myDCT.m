function C = myDCT(A)
    N = length(A);
    C = zeros(N,N);
    
    for u = 0 : N-1
        for v = 0 : N-1
            C(u+1,v+1) = sum(sum(A.*DCT_basis(u,v,N)));
        end 
    end
    
    % Normalization 
    C = C./16;
    C(1,:) = C(1,:)./2;
    C(:,1) = C(:,1)./2;
    C = round(C);
end