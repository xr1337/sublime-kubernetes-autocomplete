import sublime_plugin
import sublime

key_list = ["apiVersion", "kind", "metadata","creationTimestamp","name","spec","status","spec","type","ports","port","targetPort","selector","replicas","matchLabels","template","labels","containers","image","containerPort","readinessProbe","httpGet","path","livenessProbe","protocol","subsets","addresses","ip","externalName","clusterIP","loadBalancerIP","ingress","loadBalancer","annotations","externalIPs","revision","items","sleep","env","value","command","envFrom","imagePullPolicy","lifecycle","resources","securityContext","capabilities","stdin","stdinOnce","terminationMessagePath","terminationMessagePolicy","tty","volumeDevices","volumeMounts","mountPath","workingDir","concurrencyPolicy","failedJobsHistoryLimit","jobTemplate","schedule","startingDeadlineSeconds","successfulJobsHistoryLimit","suspend","lastScheduleTime","active","minReadySeconds","revisionHistoryLimit","updateStrategy","collisionCount","conditions","currentNumberScheduled","desiredNumberScheduled","numberAvailable","numberMisscheduled","numberReady","numberUnavailable","observedGeneration","updatedNumberScheduled","paused","progressDeadlineSeconds","strategy","availableReplicas","readyReplicas","unavailableReplicas","updatedReplicas","rollingUpdate","activeDeadlineSeconds","affinity","automountServiceAccountToken","dnsConfig","dnsPolicy","hostAliases","hostIPC","hostNetwork","hostPID","hostname","imagePullSecrets","initContainers","nodeName","nodeSelector","priority","priorityClassName","readinessGates","restartPolicy","schedulerName","serviceAccount","serviceAccountName","shareProcessNamespace","subdomain","terminationGracePeriodSeconds","tolerations","volumes","requests","limits","minReplicas","maxReplicas","metrics", "targetAverageUtilization", "scaleTargetRef",]
annotation_list = ["service.beta.kubernetes.io/aws-load-balancer-type","service.beta.kubernetes.io/aws-load-balancer-internal","service.beta.kubernetes.io/aws-load-balancer-proxy-protocol","service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval","service.beta.kubernetes.io/aws-load-balancer-access-log-enabled","service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-name","service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-prefix","service.beta.kubernetes.io/aws-load-balancer-connection-draining-enabled","service.beta.kubernetes.io/aws-load-balancer-connection-draining-timeout","service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout","service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled","service.beta.kubernetes.io/aws-load-balancer-extra-security-groups","service.beta.kubernetes.io/aws-load-balancer-security-groups","service.beta.kubernetes.io/aws-load-balancer-ssl-cert","service.beta.kubernetes.io/aws-load-balancer-ssl-ports","service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy","service.beta.kubernetes.io/aws-load-balancer-backend-protocol","service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags","service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold","service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold","service.beta.kubernetes.io/aws-load-balancer-healthcheck-timeout","service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval", "external-dns.alpha.kubernetes.io/hostname","external-dns.alpha.kubernetes.io/ttl","alb.ingress.kubernetes.io/scheme","alb.ingress.kubernetes.io/target-type", "alb.ingress.kubernetes.io/subnets", "alb.ingress.kubernetes.io/tags","alb.ingress.kubernetes.io/listen-ports","alb.ingress.kubernetes.io/ssl-policy", "alb.ingress.kubernetes.io/unhealthy-threshold-count","alb.ingress.kubernetes.io/load-balancer-attributes", "alb.ingress.kubernetes.io/certificate-arn","alb.ingress.kubernetes.io/backend-protocol","alb.ingress.kubernetes.io/healthcheck-interval-seconds","alb.ingress.kubernetes.io/healthcheck-path","alb.ingress.kubernetes.io/healthcheck-port","alb.ingress.kubernetes.io/healthcheck-protocol","alb.ingress.kubernetes.io/healthcheck-timeout-seconds","alb.ingress.kubernetes.io/healthy-threshold-count","alb.ingress.kubernetes.io/target-group-attributes"]
value_list = ["Namespace", "LoadBalancer","Pod","Service","ConfigMap"]

class KubernetesManifestCompletions(sublime_plugin.EventListener):
    def __init__(self):
      self.class_completions = [("%s \tKubernetes Keys" % s, s) for s in key_list]
      self.value_completions = [("%s \tKubernetes Values" % s, s) for s in value_list]
      self.annotation_completions = [("%s \tKubernetes Annotations" % s, s) for s in annotation_list]


    def on_query_completions(self, view, prefix, locations):
      scope = view.scope_name(view.sel()[0].b).strip()
      if(scope == "source.yaml"):
        line   = view.substr(view.line(view.sel()[0]))
        if(":" not in line):
          return self.class_completions + self.annotation_completions
        else:
          # handle this later
          # return self.value_completions
          return []
      else:
        return []
