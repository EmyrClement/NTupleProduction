#ifndef BTAGWEIGHT_H
#define BTAGWEIGHT_H

#include "DataFormats/PatCandidates/interface/Jet.h"
/**
 * Original by Andrea Rizzi
 * Modified by Lukasz Kreczko
 */

class BTagWeight {
public:
	BTagWeight( std::string MCSampleTag );

	double weight(const pat::JetCollection&) const;

	void setNumberOfBtags(unsigned int min, unsigned int max);

	bool filter(unsigned int t) const;

	double getEfficiency( const unsigned int, const pat::Jet& jet ) const;
	std::vector<double> getScaleFactor( const double, const pat::Jet& jet ) const;

	std::vector<double> getBScaleFactor(const pat::Jet& jet, double uncertaintyFactor = 1.) const;
	double getBEfficiency(const pat::Jet& jet) const;
	std::vector<double> getCScaleFactor(const pat::Jet& jet) const;
	double getCEfficiency(const pat::Jet& jet) const;
	std::vector<double> getUDSGScaleFactor(const pat::Jet& jet) const;
	double getUDSGEfficiency(const pat::Jet& jet) const;

	double getMeanUDSGScaleFactor(double jetPT, double jetEta) const;
	double getMinUDSGScaleFactor(double jetPT, double jetEta) const;
	double getMaxUDSGScaleFactor(double jetPT, double jetEta) const;

	double getMeanUDSGEfficiency(double jetPT) const;
private:
	unsigned int minNumberOfTags_;
	unsigned int maxNumberOfTags_;
	std::string MCSampleTag_;

};

std::vector<double> BjetWeights(const pat::JetCollection&, unsigned int numberOfBtags, std::string MCSampleTag);
#endif

