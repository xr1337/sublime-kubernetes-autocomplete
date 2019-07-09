import sublime_plugin
import sublime

# to which code scopes apply the code
scopes = ["source.yaml"]

# syntax keys
key_list = [
    "app",
    "active",
    "activeDeadlineSeconds",
    "addresses",
    "affinity",
    "annotations",
    "apiVersion",
    "automountServiceAccountToken",
    "availableReplicas",
    "capabilities",
    "clusterIP",
    "collisionCount",
    "command",
    "concurrencyPolicy",
    "conditions",
    "containerPort",
    "containers",
    "creationTimestamp",
    "currentNumberScheduled",
    "desiredNumberScheduled",
    "dnsConfig",
    "dnsPolicy",
    "env",
    "envFrom",
    "externalIPs",
    "externalName",
    "failedJobsHistoryLimit",
    "fieldRef",
    "fieldPath",
    "hostAliases",
    "hostIPC",
    "hostname",
    "hostNetwork",
    "hostPID",
    "httpGet",
    "image",
    "imagePullPolicy",
    "imagePullSecrets",
    "ingress",
    "initContainers",
    "ip",
    "items",
    "jobTemplate",
    "kind",
    "labels",
    "lastScheduleTime",
    "lifecycle",
    "limits",
    "livenessProbe",
    "loadBalancer",
    "loadBalancerIP",
    "matchLabels",
    "minAvailable",
    "maxReplicas",
    "metadata",
    "metrics",
    "minReadySeconds",
    "minReplicas",
    "mountPath",
    "name",
    "nodeName",
    "nodeSelector",
    "numberAvailable",
    "numberMisscheduled",
    "numberReady",
    "numberUnavailable",
    "observedGeneration",
    "path",
    "paused",
    "port",
    "ports",
    "priority",
    "priorityClassName",
    "progressDeadlineSeconds",
    "protocol",
    "readinessGates",
    "readinessProbe",
    "readyReplicas",
    "replicas",
    "requests",
    "resources",
    "restartPolicy",
    "revision",
    "revisionHistoryLimit",
    "rollingUpdate",
    "scaleTargetRef",
    "schedule",
    "schedulerName",
    "securityContext",
    "selector",
    "serviceAccount",
    "serviceAccountName",
    "shareProcessNamespace",
    "sleep",
    "spec",
    "spec",
    "startingDeadlineSeconds",
    "status",
    "stdin",
    "stdinOnce",
    "strategy",
    "subdomain",
    "subsets",
    "successfulJobsHistoryLimit",
    "suspend",
    "targetAverageUtilization",
    "targetPort",
    "template",
    "terminationGracePeriodSeconds",
    "terminationMessagePath",
    "terminationMessagePolicy",
    "tolerations",
    "tty",
    "type",
    "unavailableReplicas",
    "updatedNumberScheduled",
    "updatedReplicas",
    "updateStrategy",
    "value",
    "valueFrom",
    "volumeDevices",
    "volumeMounts",
    "volumes",
    "workingDir",
    "persistentVolumeClaimSpec",
    "accessModes",
    "resources",
    "requests",
    "storage",
    "storageClassName",
    "cpu",
    "memory",
    "affinity",
    "requiredDuringSchedulingIgnoredDuringExecution",
    "preferredDuringSchedulingIgnoredDuringExecution",
    "labelSelector",
    "matchExpressions",
    "key",
    "operator",
    "values",
    "topologyKey",
]

# annotations completions
annotation_list = [
    "alb.ingress.kubernetes.io/backend-protocol",
    "alb.ingress.kubernetes.io/certificate-arn",
    "alb.ingress.kubernetes.io/healthcheck-interval-seconds",
    "alb.ingress.kubernetes.io/healthcheck-path",
    "alb.ingress.kubernetes.io/healthcheck-port",
    "alb.ingress.kubernetes.io/healthcheck-protocol",
    "alb.ingress.kubernetes.io/healthcheck-timeout-seconds",
    "alb.ingress.kubernetes.io/healthy-threshold-count",
    "alb.ingress.kubernetes.io/listen-ports",
    "alb.ingress.kubernetes.io/load-balancer-attributes",
    "alb.ingress.kubernetes.io/scheme",
    "alb.ingress.kubernetes.io/ssl-policy",
    "alb.ingress.kubernetes.io/subnets",
    "alb.ingress.kubernetes.io/tags",
    "alb.ingress.kubernetes.io/target-group-attributes",
    "alb.ingress.kubernetes.io/target-type",
    "alb.ingress.kubernetes.io/unhealthy-threshold-count",
    "external-dns.alpha.kubernetes.io/hostname",
    "external-dns.alpha.kubernetes.io/ttl",
    "service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval",
    "service.beta.kubernetes.io/aws-load-balancer-access-log-enabled",
    "service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-name",
    "service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-prefix",
    "service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags",
    "service.beta.kubernetes.io/aws-load-balancer-backend-protocol",
    "service.beta.kubernetes.io/aws-load-balancer-connection-draining-enabled",
    "service.beta.kubernetes.io/aws-load-balancer-connection-draining-timeout",
    "service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout",
    "service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled",
    "service.beta.kubernetes.io/aws-load-balancer-extra-security-groups",
    "service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold",
    "service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval",
    "service.beta.kubernetes.io/aws-load-balancer-healthcheck-timeout",
    "service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold",
    "service.beta.kubernetes.io/aws-load-balancer-internal",
    "service.beta.kubernetes.io/aws-load-balancer-proxy-protocol",
    "service.beta.kubernetes.io/aws-load-balancer-security-groups",
    "service.beta.kubernetes.io/aws-load-balancer-ssl-cert",
    "service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy",
    "service.beta.kubernetes.io/aws-load-balancer-ssl-ports",
    "service.beta.kubernetes.io/aws-load-balancer-type",
]

value_list = [
    "Always",
    "ClusterRole",
    "ClusterRoleBinding",
    "ConfigMap",
    "CronJob",
    "DaemonSet",
    "Deployment",
    "IfNotPresent",
    "Job",
    "LoadBalancer",
    "Namespace",
    "Pod",
    "PodDisruptionBudget",
    "ReplicaSet",
    "ReplicationController",
    "Service",
    "ServiceAccount",
    "StatefulSet",
]


class KubernetesManifestCompletions(sublime_plugin.EventListener):
    def __init__(self):
        self.class_completions = [("%s \tKubernetes Keys" % s, s) for s in key_list]
        self.value_completions = [("%s \tKubernetes Values" % s, s) for s in value_list]
        self.annotation_completions = [
            ("%s \tKubernetes Annotations" % s, s) for s in annotation_list
        ]

    def on_query_completions(self, view, prefix, locations):
        scope = view.scope_name(view.sel()[0].b).strip()
        if scope in scopes:
            line = view.substr(view.line(view.sel()[0]))
            if ":" not in line:
                return self.class_completions + self.annotation_completions

        return []
