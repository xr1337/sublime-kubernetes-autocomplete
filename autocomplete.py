import sublime_plugin
import sublime

key_list = ["apiVersion", "kind", "metadata","creationTimestamp","name","spec","status","spec","type","ports","port","targetPort","selector","replicas","matchLabels","template","labels","containers","image","containerPort","readinessProbe","httpGet","path","livenessProbe","protocol","subsets","addresses","ip","type","externalName","clusterIP","loadBalancerIP","type","ingress","loadBalancer","ingress","annotations","externalIPs","revision","items","sleep","env","value","command","envFrom","imagePullPolicy","lifecycle","resources","securityContext","stdin","stdinOnce","terminationMessagePath","terminationMessagePolicy","tty","volumeDevices","volumeMounts","workingDir","concurrencyPolicy","failedJobsHistoryLimit","jobTemplate","schedule","startingDeadlineSeconds","successfulJobsHistoryLimit","suspend","lastScheduleTime","active","minReadySeconds","revisionHistoryLimit","updateStrategy","collisionCount","conditions","currentNumberScheduled","desiredNumberScheduled","numberAvailable","numberMisscheduled","numberReady","numberUnavailable","observedGeneration","updatedNumberScheduled","paused","progressDeadlineSeconds","strategy","availableReplicas","readyReplicas","unavailableReplicas","updatedReplicas","rollingUpdate","activeDeadlineSeconds","affinity","automountServiceAccountToken","dnsConfig","dnsPolicy","hostAliases","hostIPC","hostNetwork","hostPID","hostname","imagePullSecrets","initContainers","nodeName","nodeSelector","priority","priorityClassName","readinessGates","restartPolicy","schedulerName","serviceAccount","serviceAccountName","shareProcessNamespace","subdomain","terminationGracePeriodSeconds","tolerations","volumes"]
value_list = ["Namespace", "LoadBalancer","Pod","Service"]

class BootstrapCompletions(sublime_plugin.EventListener):
    def __init__(self):
      self.class_completions = [("%s \tKubernetes Keys" % s, s) for s in key_list]
      self.value_completions = [("%s \tKubernetes Values" % s, s) for s in value_list]

    def on_query_completions(self, view, prefix, locations):
      scope = view.scope_name(view.sel()[0].b).strip()
      if(scope == "source.yaml"):
        line   = view.substr(view.line(view.sel()[0]))
        if(":" not in line):
          return self.class_completions
        else:
          # return self.value_completions
          return []
      else:
        return []
