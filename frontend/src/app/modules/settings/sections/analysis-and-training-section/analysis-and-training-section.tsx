import React, { Component } from "react";
import CircleSpinner from "app/common/components/circle-spinner/circle-spinner";
import SettingsFilter from "app/modules/settings/parts/filter/filter";
import "app/modules/settings/sections/analysis-and-training-section/analysis-and-training-section.scss";
import { SettingsSections } from "app/common/store/settings/types";
import {
	uploadSettingsATFilterData,
	sendSettingsATFiltersData,
} from "app/common/store/settings/thunks";
import { uploadSettingsTrainingData } from "app/modules/settings/parts/training/store/thunks";
import { connect, ConnectedProps } from "react-redux";
import { RootStore } from "app/common/types/store.types";
import { HttpStatus } from "app/common/types/http.types";
import SettingsTraining from "app/modules/settings/parts/training/training";

class AnalysisAndTrainingSection extends Component<Props> {
	componentDidMount = () => {
		const { uploadSettingsATFilterData, uploadSettingsTrainingData } = this.props;
		// eslint-disable-next-line @typescript-eslint/no-floating-promises
		uploadSettingsATFilterData();
		// eslint-disable-next-line @typescript-eslint/no-floating-promises
		uploadSettingsTrainingData();
	};

	render() {
		const { status, trainingStatus, sendSettingsATFiltersData } = this.props;

		return (
			<div className="analysis-and-training-section">
				{status[SettingsSections.filters] === HttpStatus.FINISHED && (
					<div className="analysis-and-training-section__filter">
						<SettingsFilter
							section={SettingsSections.filters}
							saveDataFunc={sendSettingsATFiltersData}
						/>
					</div>
				)}
				{status[SettingsSections.filters] === HttpStatus.RELOADING && (
					<div className="analysis-and-training-section__spinner">
						<CircleSpinner alignCenter />
					</div>
				)}
				{Object.values(trainingStatus).reduce(
					(prevVal, item) => prevVal && item === HttpStatus.FINISHED,
					true
				) && (
					<div className="analysis-and-training-section__training">
						<SettingsTraining />
					</div>
				)}
				{Object.values(trainingStatus).reduce(
					(prevVal, item) =>
						(prevVal || item === HttpStatus.RELOADING) && item !== HttpStatus.FAILED,
					false
				) && (
					<div className="analysis-and-training-section__spinner">
						<CircleSpinner alignCenter />
					</div>
				)}
			</div>
		);
	}
}
const mapStateToProps = ({ settings }: RootStore) => ({
	status: settings.settingsStore.status,
	trainingStatus: settings.settingsTrainingStore.status,
});

const mapDispatchToProps = {
	uploadSettingsATFilterData,
	uploadSettingsTrainingData,
	sendSettingsATFiltersData,
};

const connector = connect(mapStateToProps, mapDispatchToProps);

type PropsFromRedux = ConnectedProps<typeof connector>;
type Props = PropsFromRedux & unknown;

export default connector(AnalysisAndTrainingSection);
