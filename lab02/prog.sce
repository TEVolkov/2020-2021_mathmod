s = 7.6;
fi = 3*%pi/4;

function dr=f(tetha, r)
    dr=r/2.4;
endfunction;

//r0 = s/3.6; //первый случай
//tetha0 = 0;

r0 = s/1.6;      //второй случай
tetha0 = -%pi;

tetha = 0:0.01:2*%pi;

r=ode(r0,tetha0,tetha,f);

function xt=f2(t)
    xt=tan(fi)*t;
endfunction

t = 0:1:1000;

polarplot(tetha,r,style = color('green'));
plot2d(t,f2(t),style = color('red'));
