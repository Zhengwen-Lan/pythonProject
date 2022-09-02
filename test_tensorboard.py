from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

for i in range(100):
    writer.add_scalar("y=x",scalar_value=2*i,global_step=i)

writer.close()


