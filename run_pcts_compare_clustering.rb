reals = []
final_data = []
pcts = []
1.upto(9) do |pct|
  pct = pct/10.0
  results = `python compare_clustering_coefficient.py "data/soc-Epinions1.txt" #{pct} false`.split("\n")
  reals << results.first.to_f
  final_data << results[1..-1].collect(&:to_f)
  pcts << pct
end
