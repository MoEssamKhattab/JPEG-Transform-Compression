function b = DCT_basis(u,v,N)
    b = zeros(N,N);
    for x = 0:N-1
        for y = 0:N-1
            b(x+1,y+1) = cos((2*x+1)*u*pi/(2*N))*cos((2*y+1)*v*pi/(2*N));
        end
    end
end