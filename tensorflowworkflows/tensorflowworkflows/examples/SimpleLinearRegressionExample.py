from tensorflowworkflows.regression.SimpleLinearRegression import SimpleLinearRegression

x = [[0], [1], [2]]
y = [0, 1, 2]
test_x = x
test_y = y

regressionRunner = SimpleLinearRegression("TF-OLS")

result = regressionRunner.doRegression(x, y)
print("Single regression result: "+str(result))
print()
pipelineResult = regressionRunner.doRegressionPipeline(x, y, test_x, test_y)
print("Pipeline result: "+str(pipelineResult))