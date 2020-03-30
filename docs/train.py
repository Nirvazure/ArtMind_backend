# 1. set random.seed and cudnn performance
random.seed(config.seed)
np.random.seed(config.seed)
torch.manual_seed(config.seed)
torch.cuda.manual_seed_all(config.seed)
os.environ["CUDA_VISIBLE_DEVICES"] = config.gpus
torch.backends.cudnn.benchmark = True

# 2. evaluate func


def evaluate(val_loader, model, criterion):
    # 2.1 define meters
    losses = AverageMeter()
    top1 = AverageMeter()
    top2 = AverageMeter()
    # 2.2 switch to evaluate mode and confirm model has been transfered to cuda
    model.cuda()
    model.eval()
    with torch.no_grad():
        for i, (input, target) in enumerate(val_loader):
            input = Variable(input).cuda()
            target = Variable(torch.from_numpy(np.array(target)).long()).cuda()
            # 2.2.1 compute output
            output = model(input)
            loss = criterion(output, target)
            # 2.2.2 measure accuracy and record loss
            precision1, precision2 = accuracy(output, target, topk=(1, 2))
            losses.update(loss.item(), input.size(0))
            top1.update(precision1[0], input.size(0))
            top2.update(precision2[0], input.size(0))
    return [losses.avg, top1.avg, top2.avg]


# 创建模型
model = StyleNet(num_classes=18)
# 检查CUDA可用性
if torch.cuda.is_available():
    model.cuda()
# 定义优化器设定学习率等参数
optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)
# 定义损失函数（这里是交叉熵）
loss_fn = nn.CrossEntropyLoss()
