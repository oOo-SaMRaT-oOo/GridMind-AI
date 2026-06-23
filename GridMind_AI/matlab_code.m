out = sim("simulink_model.slx");
df = out.df;
t = out.tout;
save("recovery_test_1.mat","df","t")

