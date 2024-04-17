from constructs import Construct

from aws_cdk import (
    Stack,
    # aws_sqs as sqs,
)


from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
class AwsCodepipelineTutorialStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, "Pipeline",
                                pipeline_name="MyServicePipeline",
                                synth=ShellStep("Synth",
                                    input=CodePipelineSource.connection("HassanMSh/aws-codepipeline-tutorial", "main"),
                                    commands=["npm instal -g aws-cdk", 
                                              "python -m pip install -r requirements.txt", 
                                              "cdk synth"]
                                    )
                                )